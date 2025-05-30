
package org.apache.commons.cli;

import java.util.Properties;

public interface CommandLineParser {

    CommandLine parse(Options options, String[] arguments)
               throws ParseException;


    CommandLine parse(Options options, String[] arguments, 
                      Properties properties)
               throws ParseException;


    CommandLine parse(Options options, String[] arguments, 
                      boolean stopAtNonOption)
               throws ParseException;


    CommandLine parse(Options options, String[] arguments, 
                      Properties properties, boolean stopAtNonOption)
               throws ParseException;
}