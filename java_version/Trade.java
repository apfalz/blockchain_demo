package blockchain_demo;

public class Trade{
    public Person sender;
    public Person recipient;
    public int    amount;

    public Trade(Person sender, Person recipient, int amount){
      this.sender    = sender;
      this.recipient = recipient;
      this.amount    = amount;
    }
}
