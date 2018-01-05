package domain;

public interface Observer <T> {
    void update(Observable<T> observable);
}