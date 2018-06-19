package blockchain_demo;

public class Exchange{

    public String  name;
    public Network connection_to_network;
    public int     verbose;

    public Exchange(String name, Network network){
        this.name                  = name;
        this.connection_to_network = network;
        this.verbose               = 2;
    }

    public void broadcast_request(Trade trade_instance){
        this.connection_to_network.requested_transactions.add(trade_instance);
    }

    public boolean receive_request(Trade trade_instance){
        if (trade_instance.amount <= trade_instance.sender.coin_possessed){
            this.broadcast_request(trade_instance);
            return true;
        }else{
            if (this.verbose >= 2){
                System.out.println("Detected fraudulent transaction!");
            }
            return false;
        }
    }
}
