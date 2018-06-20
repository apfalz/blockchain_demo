package blockchain_demo;

public class Blockchain_Demo{

    public static void main(String args[]){
        System.out.println("Starting demo.");
        Network         net      = new Network();

        Exchange        exchange = new Exchange("demo_exchange", net);

        Threaded_People people   = new Threaded_People(exchange);

        Threaded_Miner miner_0   = new Threaded_Miner("miner_0", net);
        Threaded_Miner miner_1   = new Threaded_Miner("miner_1", net);


        people.start();
        miner_0.start();
        miner_1.start();
    }

}
