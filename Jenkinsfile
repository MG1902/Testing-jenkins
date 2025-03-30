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
                sh 'python3 Main.py'
            }
        }
    }
    
}