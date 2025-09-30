pipeline {
  agent any

  parameters {
    string(name: 'IMAGE_TAG', defaultValue: 'latest', description: 'Image tag from GitHub Actions')
  }

  environment {
    IMAGE = "ghcr.io/${GITHUB_REPOSITORY_OWNER}/titanic:${params.IMAGE_TAG}"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Pull & Test image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'ghcr-token', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh '''
            echo $PASS | docker login ghcr.io -u $USER --password-stdin
            docker pull $IMAGE
            docker run --rm $IMAGE pytest tests/
          '''
        }
      }
    }

    stage('Run Prefect flow') {
      steps {
        sh '''
          docker run --rm \
            -e PREFECT_API_URL=http://host.docker.internal:4200/api \
            $IMAGE \
            python -m flows.pipeline_flow
        '''
      }
    }
  }

  post {
    always {
      // Récupère les artefacts générés dans le conteneur
      sh 'docker run --rm -v $(pwd):/output $IMAGE cp model.pkl submission.csv /output/ || true'
      archiveArtifacts artifacts: 'model.pkl,submission.csv', fingerprint: true
    }
  }
}

