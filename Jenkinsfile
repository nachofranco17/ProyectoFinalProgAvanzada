pipeline {
    agent any
    
    parameters {
        choice(
            name: 'Opcion',
            choices: ['Trivia', 'Procesar Pedidos', 'Consultas USQL'],
            description: '---------- Elige una opción para ejecutar -------------'
        )
    }

    
    stages {
        stage('Selección de Opción') {
            steps {
                script {
                    echo "--------------------------------------"
                    echo "Opción seleccionada: ${params.Opcion}"
                    echo "--------------------------------------"
                }
            }
        }

        stage('Instalar Dependencias') {
            steps {
                dir('Entregable1') {

                    // Acá tuve que poner la ubicación entera de python.exe porque no me lo reconocía como comando
                    bat 'C:\\Users\\ignac\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m pip install -r requirements.txt'
                }
            }
        }

        stage('Ejecutar Opción Seleccionada') {
            steps {
                script {
                    if (params.Opcion == 'Trivia') {
                        
                        echo "--------------------------------------"
                        echo 'Ejecutando el juego de Trivia...'
                        echo "--------------------------------------"
                        
                        // Acá se ejecuta el código correspondiente al trivia
                        
                        dir('Entregable1') {

                            // Mismo tema con la ubicación de python.exe
                            bat 'C:\\Users\\ignac\\AppData\\Local\\Programs\\Python\\Python310\\python.exe Principal.py'
                        }
                        
                    } else if (params.Opcion == 'Procesar Pedidos') {
                        
                        echo "--------------------------------------"
                        echo 'Procesando pedidos...'
                        echo "--------------------------------------"
                        
                        // Acá se ejecuta el código correspondiente al procesamiento de pedidos
                        
                    } else if (params.Opcion == 'Consultas USQL') {
                        
                        echo "--------------------------------------"
                        echo 'Ejecutando consultas USQL...'
                        echo "--------------------------------------"
                        
                        // Acá se ejecuta el código correspondiente a las consultas USQL
                        
                        // sh 'git clone https://github.com/tu_usuario/entregable3_usql.git'
                        // sh 'python entregable3_usql/main.py'
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo "--------------------------------------"
            echo 'Pipeline completado con éxito.'
            echo "--------------------------------------"
        }
        failure {
            echo "--------------------------------------"
            echo 'Hubo un error en el pipeline.'
            echo "--------------------------------------"
        }
    }
}