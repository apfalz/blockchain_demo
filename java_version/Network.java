package blockchain_demo;
import java.util.*;

public class Network{
    public Block             newest_block;
    public ArrayList<Miner>  connected_miners;
    public int               num_miners;
    public int               verbose;
    public ArrayList<Block>  list_of_mined_blocks;
    public ArrayList<Trade>  requested_transactions;

    public Network(Block genesis_block){
        this.newest_block           = genesis_block;
        this.connected_miners       = new ArrayList<Miner>();
        this.requested_transactions = new ArrayList<Trade>();
        this.list_of_mined_blocks   = new ArrayList<Block>();
        this.verbose                = 2;
        this.num_miners             = 0;

    }

    public void establish_connection(Miner miner){
        if (this.verbose >= 1){
            System.out.println("Network received a new connection from " + miner.name);
        }
        this.connected_miners.add(miner);
        this.num_miners += 1;
    }

    public void receive_new_block(Block block, String miner_name){
        if(this.verbose >= 1){
            System.out.println("Network received a new block! Broadcasting to all miners on network.");
        }
        this.newest_block = block;
        this.list_of_mined_blocks.add(block);
        for(Miner temp : this.connected_miners){
            if (temp.name != miner_name){
                temp.receive_new_block(block);
            }
        }
    }
}
