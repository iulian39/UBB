package domain;

import java.io.BufferedReader;

public class FileData{
    private String fileName;
    private BufferedReader fileDescriptor;

    public FileData() {}

    public FileData(String fr, BufferedReader fd)
    {
        fileName = fr;
        fileDescriptor = fd;
    }

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public BufferedReader getFileDescriptor() {
        return fileDescriptor;
    }

    public void setFileDescriptor(BufferedReader fileDescriptor) {
        this.fileDescriptor = fileDescriptor;
    }

//    public String toString()
//    {
//		return fileDescriptor;
//    }
}