package domain.Statements;

import domain.MyDictionary;
import domain.MyStack;
import domain.PrgState;

import java.util.Deque;

public class forkStmt implements IStatement {
        private IStatement stmt;
        public forkStmt(IStatement stmt) {
            this.stmt = stmt;
        }

        @Override
        public PrgState execute(PrgState state) {
            MyStack<IStatement> s = new MyStack<>();
            s.push(stmt);
            PrgState forkProgram = new PrgState(s, state.get_symbolTable().clone(), state.get_messages(), this.stmt, state.getFileTable(), state.getHeap(), state.getId() * 10);
            return forkProgram;
        }

        @Override
        public String toString() {
            return "fork(" + this.stmt.toString() + ")";
        }
}
