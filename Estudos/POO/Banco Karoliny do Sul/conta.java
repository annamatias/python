class Conta {

    //atributos
    private int numero;
    private String titular;
    private double saldo;
    private double limite;

    //construtor
    Conta(int numero, String titular, double saldo, double limite) {
        this.numero = numero;
        this.titular = titular;
        this.saldo = saldo;
        this.limite = limite;
    }
}
    //metodos
    void extrato() {
        System.out.println("Saldo de " + this.saldo)
    }


    public double getLimite() {
        return limite;
    }

    public void setLimite(double limite) {
        this.limite = limite;
    }

    public double getNumero() {
        return numero;
    }

    public void getTitular() {
        return titular;
    }

    public double getSaldo() {
        return saldo;
    }

    public static String codigo() {
        return "001"
    }

Conta contaDoNico = new Conta(123, "Nico", 55.5, 1000.0);
contaDoNico.deposita(100.0);