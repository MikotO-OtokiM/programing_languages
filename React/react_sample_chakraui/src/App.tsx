import { ChakraProvider } from '@chakra-ui/react';
import { BrowserRouter } from 'react-router-dom';

import theme from "./theme/theme";
import { Router } from './router/Router';

function App() {
  return (
    /**
     * Chakura UI を利用する場合は、ルートのコンポーネントを ChakuraProvider の
     * タグで囲う必要あり
     * theme 属性で作成したグローバルのスタイルを適用する
     */
    <ChakraProvider theme={theme}>
      {/*
      画面遷移で react-router-dom を利用する場合は、遷移画面を
      BrowserRouter タグで囲う必要あり
      */}
      <BrowserRouter>
        <Router />
      </BrowserRouter>
    </ChakraProvider>
  );
}

export default App;
