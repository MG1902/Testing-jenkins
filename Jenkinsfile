pipeline {
    agent any
    stages {
        stage('Check Python Version') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 --version'  // Linux/Mac
                    } else {
                        bat 'python --version'  // Windows
                    }
                }
            }
        }
        stage('Run Main.py') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 main.py'  // Linux/Mac
                    } else {
                        bat 'python main.py'  // Windows
                    }
                }
            }
        }
    }
}
