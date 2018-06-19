package blockchain_demo;

public class Person{

    public String name;
    public int    coin_possessed;
    public int    address;

    public Person(int coin_possessed, int address, String name){
        this.name           = name;
        this.coin_possessed = coin_possessed;
        this.address        = address;
    }

    public void request_trade(Exchange exchange, Person recipient, int amount){
        this.coin_possessed -= amount;
    }

    public void receive_trade(int amount){
        this.coin_possessed += amount;
    }


}
