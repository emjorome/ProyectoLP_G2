fun main() {
    var a = 10
    var b = 20
    var c = a + b * 2

    if (c >= 30 && b != 0) {
        println("Resultado: $c")
    } else {
        println("Valor de b es cero")
    }
    for (i in 1..5) {
        println("Iteracion $i")
    }
}