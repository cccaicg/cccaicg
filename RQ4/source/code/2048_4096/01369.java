/**
 * 统一线程处理
 * @param <T>
 * @return
 */
public static <T> FlowableTransformer<T, T> rxSchedulerHelper(){    //compose简化线程
    return new FlowableTransformer<T, T>() {
        @Override
        public Flowable<T> apply(Flowable<T> observable) {
            return observable.subscribeOn(Schedulers.io())
                    .observeOn(AndroidSchedulers.mainThread());
        }
    };
}