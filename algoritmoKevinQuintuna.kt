// Clase con propiedades y funciones
class Calculator {
    var history: MutableList<String> = mutableListOf()

    // Función para sumar
    fun add(a: Int, b: Int): Int {
        val result = a + b
        history.add("Sum: $a + $b = $result")
        return result
    }

    // Función para multiplicar
    fun multiply(a: Int, b: Int): Int {
        val result = a * b
        history.add("Multiply: $a * $b = $result")
        return result
    }

    // Función para mostrar el historial
    fun showHistory() {
        history.forEach { println(it) }
    }
}

// Función principal
fun main() {
    val calc = Calculator()
    
    val x = 15
    val y = 10
    val sum = calc.add(x, y)
    val product = calc.multiply(x, y)
    
    // Expresiones condicionales
    if (sum > 20) {
        println("The sum is greater than 20")
    } else {
        println("The sum is less or equal to 20")
    }

    // Expresión when
    when {
        product % 2 == 0 -> println("The product is even")
        else -> println("The product is odd")
    }

    // Bucle con lambda
    (1..5).forEach { i ->
        println("Lambda iteration: $i")
    }

    // Uso de una función anónima
    val square = { num: Int -> num * num }
    println("Square of 5: ${square(5)}")
    
    // Invocar el historial
    calc.showHistory()
}
