pipeline {
    agent any

    environment {
        // Define any environment variables if needed
    }

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
                        sh 'python test.py'
                    } catch (Exception e) {
                        echo "Failed to execute Main.py: ${e}"
                        writeFile file: 'Report.txt', text: "Failed to execute Main.py: ${e}"
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
