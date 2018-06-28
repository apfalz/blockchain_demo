package blockchain_demo;
import java.util.*;
public class Blockchain_Demo{

    public static void main(String args[]){
        System.out.println("Starting demo.");
        ArrayList<Trade> trades   = new ArrayList<Trade>();
        Person          satoshi  = new Person(1, -1, "Satoshi");
        Person          nakamoto = new Person(1, -1, "Nakamoto");
        trades.add(new Trade(satoshi, nakamoto, 1));


        Block           genesis  = new Block(1, trades);
        Network         net      = new Network(genesis);

        Exchange        exchange = new Exchange("demo_exchange", net);

        Threaded_People people   = new Threaded_People(exchange);

        Threaded_Miner miner_0   = new Threaded_Miner("miner_0", net);
        Threaded_Miner miner_1   = new Threaded_Miner("miner_1", net);


        people.start();
        miner_0.start();
        miner_1.start();
    }

}
