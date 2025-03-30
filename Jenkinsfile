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
                sh 'python3 -m C:\ProgramData\Jenkins\.jenkins\workspace\Run_python_program\Main.py'
            }
        }
    }
    
}
