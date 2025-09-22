pipeline {
    agent any
    
    environment {
        PYTHON_PATH = '/usr/bin/python3'
        VENV_PATH = 'venv'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv $VENV_PATH
                    source $VENV_PATH/bin/activate
                    pip install --upgrade pip
                    pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    source $VENV_PATH/bin/activate
                    python -m pytest test_app.py -v
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                sh '''
                    source $VENV_PATH/bin/activate
                    python app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                    echo "Application deployed successfully!"
                    echo "Deployment timestamp: $(date)"
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed!'
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed!'
        }
    }
}
