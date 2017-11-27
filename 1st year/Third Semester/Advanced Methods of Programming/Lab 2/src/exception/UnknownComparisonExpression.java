package exception;

public class UnknownComparisonExpression extends RuntimeException{
    public UnknownComparisonExpression() { super(); }
    public UnknownComparisonExpression(String s) { super(s); }
}
