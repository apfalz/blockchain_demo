package blockchain_demo;
import java.util.*;

public class Miner{

    public String  name;
    public int     num_blocks_mined;
    public Block[] mined_blocks;
    public Network network;
    public Block   newest_block;
    public Boolean interrupt;
    public int     verbose;
    private Random rand;
    public ArrayList<Object> pending_trades = new ArrayList<Object>();
    //mining thread;

    public Miner(String name, Network network_connection){
        this.name             = name;
        this.num_blocks_mined = 0;

        this.network          = network_connection;
        this.network.establish_connection(this);

        this.newest_block     = this.network.newest_block;

    }

    public void start_mining(){
        this.pending_trades = this.network.requested_transactions;
        int value           = 0;
        int target          = 10;
        if (this.verbose >= 2){
            System.out.println(this.name + ": Begin mining for a new block.");
        }

        //keep working until you receive interrupt or until you find a new block.
        while (this.interrupt == false && value != target){
            try{
                Thread.sleep(rand.nextInt(10) * 1000);
                value += 1;
            }
            catch(InterruptedException ex){
                Thread.currentThread().interrupt();
            }
        }

        //if you found a new block, broadcast it and start working on next block.
        if (value == target){
            if (this.verbose >= 1){
                System.out.println(this.name + ": I found a new block! Letting network know about it.");
            }
            String temp_string = this.newest_block.toString();
            int    hash_value  = temp_string.hashCode();
            Block new_block    = new Block(hash_value, this.pending_trades);
            broadcast_new_block(new_block);
        }
        //if someone else found the block before you, update your state, then start working on the next block;
        else if (this.interrupt == true && value != target){
            if (this.verbose >= 2){
                System.out.println(this.name + ": Someone else found a block. Starting over.");
            }
            this.interrupt = false;
            this.start_mining();
        }
    }
    public void broadcast_new_block(Block block){
        this.network.receive_new_block(block, this.name);
    }

    public Boolean  receive_new_block(Block block){
        return true;
    }
}
