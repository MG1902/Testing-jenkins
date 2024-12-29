pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository containing your project
                git 'https://github.com/MG1902/Testing-jenkins.git'
            }
        }

        stage('Execute Python Scripts') {
            steps {
                script {
                    // Execute the Python scripts in the correct order
                    try {
                        bat 'python test.py'
                    } catch (Exception e) {
                        echo "Failed to execute test.py: ${e}"
                        writeFile file: 'Report.txt', text: "Failed to execute test.py: ${e}"
                        error "Pipeline failed"
                    }
                }
            }
        }
    }

    post {
        always {
            // Archive the report file
            archiveArtifacts artifacts: 'Report.txt', allowEmptyArchive: true
        }
    }
}
