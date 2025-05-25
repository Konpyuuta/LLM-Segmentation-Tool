
package org.apache.commons.cli;


public class OptionBuilder {

    private static String longopt;

    private static String description;

    private static String argName;

    private static boolean required;

    private static int numberOfArgs = Option.UNINITIALIZED;

    private static Object type;

    private static boolean optionalArg;

    private static char valuesep;

    private static OptionBuilder instance = new OptionBuilder();

    private OptionBuilder()
    {
    }


    private static void reset()
    {
        description = null;
        argName = "arg";
        longopt = null;
        type = null;
        required = false;
        numberOfArgs = Option.UNINITIALIZED;


        optionalArg = false;
        valuesep = (char) 0;
    }

    public static OptionBuilder withLongOpt(String newLongopt)
    {
        OptionBuilder.longopt = newLongopt;

        return instance;
    }

    public static OptionBuilder hasArg()
    {
        OptionBuilder.numberOfArgs = 1;

        return instance;
    }

    public static OptionBuilder hasArg(boolean hasArg)
    {
        OptionBuilder.numberOfArgs = (hasArg == true) ? 1 : Option.UNINITIALIZED;

        return instance;
    }

    public static OptionBuilder withArgName(String name)
    {
        OptionBuilder.argName = name;

        return instance;
    }

    public static OptionBuilder isRequired()
    {
        OptionBuilder.required = true;

        return instance;
    }

    public static OptionBuilder withValueSeparator(char sep)
    {
        OptionBuilder.valuesep = sep;

        return instance;
    }

    public static OptionBuilder withValueSeparator()
    {
        OptionBuilder.valuesep = '=';

        return instance;
    }

    public static OptionBuilder isRequired(boolean newRequired)
    {
        OptionBuilder.required = newRequired;

        return instance;
    }

    public static OptionBuilder hasArgs()
    {
        OptionBuilder.numberOfArgs = Option.UNLIMITED_VALUES;

        return instance;
    }

    public static OptionBuilder hasArgs(int num)
    {
        OptionBuilder.numberOfArgs = num;

        return instance;
    }

    public static OptionBuilder hasOptionalArg()
    {
        OptionBuilder.numberOfArgs = 1;
        OptionBuilder.optionalArg = true;

        return instance;
    }

    public static OptionBuilder hasOptionalArgs()
    {
        OptionBuilder.numberOfArgs = Option.UNLIMITED_VALUES;
        OptionBuilder.optionalArg = true;

        return instance;
    }

    public static OptionBuilder hasOptionalArgs(int numArgs)
    {
        OptionBuilder.numberOfArgs = numArgs;
        OptionBuilder.optionalArg = true;

        return instance;
    }

    public static OptionBuilder withType(Object newType)
    {
        OptionBuilder.type = newType;

        return instance;
    }

    public static OptionBuilder withDescription(String newDescription)
    {
        OptionBuilder.description = newDescription;

        return instance;
    }

    public static Option create(char opt)
                         throws IllegalArgumentException
    {
        return create(String.valueOf(opt));
    }

    public static Option create()
                         throws IllegalArgumentException
    {
        if (longopt == null)
        {
            throw new IllegalArgumentException("must specify longopt");
        }

        return create(null);
    }

    public static Option create(String opt)
                         throws IllegalArgumentException
    {
        Option option = new Option(opt, description);


        option.setLongOpt(longopt);
        option.setRequired(required);
        option.setOptionalArg(optionalArg);
        option.setArgs(numberOfArgs);
        option.setType(type);
        option.setValueSeparator(valuesep);
        option.setArgName(argName);


        OptionBuilder.reset();

        return option;
    }
}