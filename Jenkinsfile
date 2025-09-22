stage('Install Dependencies') {
    steps {
        echo 'Creating virtual environment and installing dependencies...'
        sh '''
            python3 -m venv venv
            source venv/bin/activate
            pip install --upgrade pip
            pip install pytest
        '''
    }
}

stage('Run Tests') {
    steps {
        echo 'Running unit tests...'
        sh '''
            source venv/bin/activate
            python -m pytest test_app.py -v
        '''
    }
}

stage('Build') {
    steps {
        echo 'Building application...'
        sh '''
            source venv/bin/activate
            python app.py
        '''
    }
}
