package blockchain_demo;
import java.util.*;

public class Block{
    public int   prev_hash;
    public int   nonce;
    public Date  timestamp;
    public int   verbose;
    public int   target;
    public ArrayList<Trade> transactions_list;




    public Block(int prev_hash, ArrayList<Trade> transactions_list){
        this.prev_hash         = prev_hash;
        this.transactions_list = transactions_list;
        this.nonce             = 0;
        this.timestamp         = new Date();
        this.target            = 10;
        this.verbose           = 2;

    }


}
