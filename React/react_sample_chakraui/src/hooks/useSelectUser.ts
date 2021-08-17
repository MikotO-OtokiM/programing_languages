// 選択したユーザー情報を特定し、モーダルを表示するカスタムフック
import { useCallback, useState } from "react"
import { User } from "../types/api/user";

type Props = {
  id: number;
  users: Array<User>;
  onOpen: () => void;
}

export const useSelectUser = () => {
  const [selectedUser, setSelectedUser] = useState<User | null>(null);

  const onSelectUser = useCallback((props: Props) => {
    const { id, users, onOpen } = props;
    const targetUser = users.find((user) => user.id === id);
    // 対象データが必ずある（undefind でないことが保証できる）場合は ! を付けて
    // 値があることを明示的に示すことで型エラーを解消できる
    setSelectedUser(targetUser!);
    onOpen();
  }, [])

  return { onSelectUser, selectedUser }
}