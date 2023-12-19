package org.clyze.doop.soot.pointans.utils;

import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.ArrayList;
import java.util.List;

/**
 * @author
 */
public class ExtClassLoader extends ClassLoader {
    private String rootDir;
    private String dependency;

    public ExtClassLoader(String rootDir, String dependency) {
        this.rootDir = rootDir;
        this.dependency = dependency;
    }

    public Class<?> findClassExt(String name) throws ClassNotFoundException {
        return findClass(name);
    }

    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {
        // System.out.println(name);
        String path = classNameToPath(rootDir, name);
        File file = new File(path);
        byte[] classData = null;
        if (file.exists()) {
            classData = getClassData(path);
        } else {
            try {
                return findClassJar(name);
            } catch (MalformedURLException e) {
                e.printStackTrace();
            }
        }
        if (classData == null) {
            throw new ClassNotFoundException();
        } else {
            return defineClass(name, classData, 0, classData.length);
        }
    }

    private byte[] getClassData(String className) {
        try {
            InputStream ins = new FileInputStream(className);
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            int bufferSize = 4096;
            byte[] buffer = new byte[bufferSize];
            int bytesNumRead = 0;
            while ((bytesNumRead = ins.read(buffer)) != -1) {
                baos.write(buffer, 0, bytesNumRead);
            }
            return baos.toByteArray();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    private String classNameToPath(String baseDir, String className) {
        return baseDir + File.separatorChar
                + className.replace('.', File.separatorChar) + ".class";
    }

    private Class<?> findClassJar(String name) throws MalformedURLException, ClassNotFoundException {
        File baseFile = new File(dependency);
        List<URL> list = new ArrayList<>();
        File[] files = baseFile.listFiles();
        for (File file : files) {
            if (file.isDirectory()) {
                continue;
            } else {
                URL url = new URL("file:" + file.getAbsolutePath());
                list.add(url);
            }
        }
        URL[] urls = new URL[list.size()];
        URLClassLoader urlClassLoader = new URLClassLoader(list.toArray(urls));
        return urlClassLoader.loadClass(name);
    }

}
