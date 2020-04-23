import java.security.NoSuchAlgorithmException;
import java.io.IOException;

// 
// Decompiled by Procyon v0.5.36
// 

public class HashCode
{
    public static void main(final String[] array) throws IOException, NoSuchAlgorithmException {
        
        final byte[] bytes = "992379d60a53006c044aabadecb1c719".getBytes();
        int i = 0;
        for (int j = 0; j < bytes.length; ++j) {
            i += (0xFE ^ bytes[j]) % 10000;
        }
        System.out.println("The flag is: SKY-JDEC-" + String.format("%04d", i) + ". Good job");
    }
}