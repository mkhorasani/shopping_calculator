import streamlit as st
import pandas as pd

st.title('ماشین حساب خرید')
st.write('___')
st.subheader('آپلود فایل')
file = st.file_uploader('لطفا فایل را آپلود کنید')

if file is not None:
    df = pd.read_excel(file)
    products_list = df['نوع کالا'].tolist()
    st.write('___')
    st.subheader('انتخاب محصولات')
    selection = st.multiselect('محصولات را انتخاب کنید',products_list)
    if selection:            
        final_df = pd.DataFrame(columns=['نوع کالا','تعداد','قیمت'])
        st.write('___')
        st.subheader('انتخاب تعداد')
        for i in range(0,len(selection)):
            final_df.loc[i,'نوع کالا'] = selection[i]
            final_df.loc[i,'تعداد'] = 1
            final_df.loc[i,'قیمت'] = df[df['نوع کالا']==selection[i]]['قیمت'].iloc[0]
        edited_df = st.data_editor(final_df,disabled=('نوع کالا', 'قیمت'))
        if edited_df is not None:
            final_df['تعداد'] = edited_df['تعداد']
            final_df['قیمت جمع'] = edited_df['تعداد']*final_df['قیمت']
        st.write('___')
        st.subheader('جدول نهایی')
        st.write(final_df)
        st.metric('قیمت کل',round(final_df['قیمت جمع'].sum(),2))
