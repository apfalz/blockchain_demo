package blockchain_demo;

public class Threaded_Miner extends Thread{

    Miner miner;

    public Threaded_Miner(String child_name, Network child_network){
        this.miner = new Miner(child_name, child_network);
    }

    public void run(){
        System.out.println("starting thread");
        this.miner.start_mining();
    }
}
