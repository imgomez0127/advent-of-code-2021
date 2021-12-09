let rec load_input (ic:in_channel) (lst: int list) : int list =
  try
    let line = (input_line ic) in
    (load_input ic ((int_of_string line)::lst))
  with e ->
    lst

let rec zip (lst1: 'a list) (lst2: 'b list) : ('a*'b) list =
  (match lst1, lst2 with
   | x::xs, y::ys -> (x,y)::(zip xs ys)
   | _, _ -> [])

let format_lst (lst: int list) : (int*int) list =
  (match lst with
   | x::xs -> (zip lst xs)
   | [] -> [])

let count_diff (lst: (int*int) list) : int =
  (List.fold_right (fun (prev, cur) acc -> if cur > prev then acc else acc+1) lst 0)

let main (file_name: string) : int =
  let ic = open_in file_name in
  let lst = (format_lst (load_input ic [])) in
  (count_diff lst)
