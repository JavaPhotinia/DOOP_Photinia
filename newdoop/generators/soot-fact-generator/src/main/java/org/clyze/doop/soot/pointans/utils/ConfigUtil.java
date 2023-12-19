package org.clyze.doop.soot.pointans.utils;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

/**
 * @ClassName   ConfigUtil
 * @Description read config
 */
public class ConfigUtil {
    public static Properties getProperties(String configPath) {
        Properties p = null;
        if (configPath == null || "".equals(configPath)) {
            return p;
        }
        try {
            InputStream in = new BufferedInputStream(new FileInputStream(configPath));
            p = new Properties();
            p.load(in);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return p;
    }
}
