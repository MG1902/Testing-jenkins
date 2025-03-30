pipeline{
    agent any
    stages{
        stage('check python version'){
         steps{
           sh 'python --version'
        }   
        }
        stage('Run Main.py')
        {
            steps
            {
                sh 'pwd'
                sh 'ls -la'
                sh 'python Main.py'
            }
        }
    }
    
}
