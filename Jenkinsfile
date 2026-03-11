pipeline {
    agent any

    environment {
        HEALING_WEBHOOK = 'http://healing-engine:5000/webhook/jenkins'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/manpritsingh-mod/Demo-test-pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests/ -v --tb=short --junit-xml=test-results.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-results.xml'
                }
            }
        }
    }

    post {
        failure {
            sh """
                echo "============================================"
                echo "BUILD FAILED — Triggering Self-Healing Engine"
                echo "============================================"
                curl -s -X POST \
                    -H 'Content-Type: application/json' \
                    -d '{"name": "${env.JOB_NAME}", "build": {"number": ${env.BUILD_NUMBER}, "status": "FAILURE", "url": "${env.BUILD_URL}"}}' \
                    ${env.HEALING_WEBHOOK} || echo "Webhook call failed (non-critical)"
            """
        }
        success {
            echo "BUILD SUCCESSFUL — All tests passed. No healing needed."
        }
    }
}
