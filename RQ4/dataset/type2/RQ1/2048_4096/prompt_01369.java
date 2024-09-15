/**
 * 统一线程处理
 * @param <T>
 * @return
 */
public static <T> FlowableTransformer<T, T> rxSchedulerHelper() 
{
    return new FlowableTransformer<T, T>()
    {
        @Override
        public Publisher<T> apply(Flowable<T> upstream)
        {
            return upstream.subscribeOn(Schedulers.io())
                    .observeOn(AndroidSchedulers.mainThread());
        }
    };
}   