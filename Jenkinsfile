pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build & Test') {
      steps {
        sh 'docker build -t titanic-local:latest .'
        sh 'docker run --rm titanic-local:latest pytest tests/'
      }
    }

    stage('Run Prefect Flow') {
      steps {
        sh '''
          docker run --rm \
            -e PREFECT_API_URL=http://host.docker.internal:4200/api \
            -v $(pwd):/output \
            titanic-local:latest \
            bash -c "python -m flows.pipeline_flow && cp model.pkl submission.csv /output/"
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'model.pkl,submission.csv', fingerprint: true
    }
  }
}