pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '''
                python -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call venv\\Scripts\\activate

                python -m pip install --upgrade pip

                pip install -r requirements.txt
                '''
            }
        }

        stage('Run All Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate

                pytest test --allure=report\\allure-results --html=reports\\html_report.html
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false,
                       jdk: '',
                       results: [[path: 'reports/allure-results']],
                       commandline: 'allure'
            }
        }
    }

    post {

        always {
            echo 'Test execution completed'
        }

        success {
            echo 'Build Passed'
        }

        failure {
            echo 'Build Failed'
        }
    }
}