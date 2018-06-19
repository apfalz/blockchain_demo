package blockchain_demo;
import java.util.*;

public class Network{
    public Block             newest_block;
    public Miner[]           connected_miners = new Miner[10];
    public int               num_miners;
    public int               verbose;
    public ArrayList<Object> list_of_mined_blocks;
    public ArrayList<Object> requested_transactions;

    public Network(){
        // this.requested_transactions = new ArrayList<Object>();
        // this.connected_miners       = new ArrayList<Object>();
        this.verbose                = 2;
        this.num_miners             = 0;
        // this.list_of_mined_blocks   = new ArrayList<Object>();
    }

    public void establish_connection(Miner miner){
        if (this.verbose >= 1){
            System.out.println("Network received a new connection from " + miner.name);
        }
        this.connected_miners[num_miners] = miner;
        this.num_miners += 1;
    }

    public void receive_new_block(Block block, String miner_name){
        if(this.verbose >= 1){
            System.out.println("Network received a new block! Broadcasting to all miners on network.");
        }
        this.newest_block = block;
        this.list_of_mined_blocks.add(block);
        for (int m = 0; m < this.connected_miners.length; m++){
            Miner temp = this.connected_miners[m];
            if (temp.name != miner_name){
                temp.receive_new_block(block);
            }
        }
    }
}
