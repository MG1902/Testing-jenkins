pipeline{
    agent any
    stages{
        stage('check python version'){
         steps{
           sh 'python3 --version'
        }   
        }
        stage('Run Main.py')
        {
            steps
            {
                sh 'pwd'
                sh 'ls -la'
                sh 'python3 Main.py'
            }
        }
    }
    
}