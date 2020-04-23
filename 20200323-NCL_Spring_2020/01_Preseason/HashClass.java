import java.security.NoSuchAlgorithmException;
import java.io.IOException;

// 
// Decompiled by Procyon v0.5.36
// 

public class HashCode
{
    public static void main(final String[] array) throws IOException, NoSuchAlgorithmException {
        if (array.length != 1) {
            System.out.println("Usage: java HashCode <tid>");
            System.exit(1);
        }
        final byte[] bytes = array[0].getBytes();
        int i = 0;
        for (int j = 0; j < bytes.length; ++j) {
            i += (0xFE ^ bytes[j]) % 10000;
        }
        System.out.println("The Java hashcode of the flag is: " + ("SKY-JDEC-" + String.format("%04d", i)).hashCode() + ". Good luck");
    }
}