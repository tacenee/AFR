import java.util.Stack;

public class offer20_包含min函数的栈 {
    Stack<Integer> data = new Stack<Integer>();
    Stack<Integer> min = new Stack<Integer>();

    public void push(int node) {
        data.push(node);
        if(min.empty()){
            min.push(node);
        }else{
            int top = (int)min.peek();
            if(top <= node){
                min.push(top);
            }else{
                min.push(node);
            }
        }
    }

    public void pop() {
        if(!(data.empty())){
            data.pop();
            min.pop();
        }
    }

    public int top() {
        return (int)data.peek();
    }

    public int min() {
        if(min.empty())
            return 0;
        return (int)min.peek();
    }
}
