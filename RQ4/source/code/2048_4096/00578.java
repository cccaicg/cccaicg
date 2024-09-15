/**
 * 设置选中状态变换监听
 *
 * @param listener
 * @return
 */
public T setOnSelectedChangeListener(OnSelectedChangeListener listener){
    this.mOnSelectedChangeListener = listener;
    return (T) this;
}