pipeline{
    agent any
    stages{
        stage('check python version'){
         steps{
           bat 'python --version'
        }   
        }
        stage('Run Main.py')
        {
            steps
            {
                bat 'python Main.py'
            }
        }
    }
    
}
