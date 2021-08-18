import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter } from 'react-router-dom';
import { Router } from './router/Router';

// デフォルトテーマ確認用
import { useTheme } from '@material-ui/core/styles';



function App() {

  // デフォルトテーマ確認用
  const theme = useTheme();
  console.log(theme);

  return (
    /**
     * Chakura UI を利用する場合は、ルートのコンポーネントを ChakuraProvider の
     * タグで囲う必要あり
     * theme 属性で作成したグローバルのスタイルを適用する
     */
    <>
      {/*
     画面遷移で react-router-dom を利用する場合は、遷移画面を
     BrowserRouter タグで囲う必要あり
     */}
      <BrowserRouter>
        <Router />
      </BrowserRouter>
    </>
  )
}

export default App;
