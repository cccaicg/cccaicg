/**
 * 设置选中状态变换监听
 *
 * @param listener
 * @return
 */
public T setOnSelectedChangeListener(OnSelectedChangeListener listener) 
{
    this.listener = listener;
    return (T) this;
}   