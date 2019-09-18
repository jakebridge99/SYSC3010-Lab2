package com.company;

import java.net.*;
import java.util.Scanner;

public class UDPSender {

    public static void main(String[] args)
    {
        // Check the arguments
        if( args.length != 2 )
        {
            System.out.println( "usage: java UDPSender host port" ) ;
            return ;
        }
        DatagramSocket socket = null ;
        try
        {
            // Convert the arguments first, to ensure that they are valid
            InetAddress host = InetAddress.getByName( args[0] ) ;
            int port         = Integer.parseInt( args[1] ) ;
            socket = new DatagramSocket() ;

            Scanner in;
            in = new Scanner (System.in);
            int messageNum;
            while (true)
            {
                System.out.println("Enter number of time (e.g. 1, 2, 3, 4, 27123176, etc) to send a message(n), -1 to quit ");
                messageNum = in.nextInt();
                if (messageNum == -1) break;
                //if (message.length()==0) break;
                //byte [] data = message.getBytes() ;
                for(int i = 0; i < messageNum; i++){
                    String temp = "message" + i;
                    byte [] data = temp.getBytes() ;
                    DatagramPacket packet = new DatagramPacket( data, data.length, host, port ) ;
                    socket.send( packet ) ;
                }


            }
            System.out.println ("Closing down");
        }
        catch( Exception e )
        {
            System.out.println( e ) ;
        }
        finally
        {
            if( socket != null )
                socket.close() ;
        }
    }
}

