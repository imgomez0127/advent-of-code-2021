let rec load_input (ic:in_channel) (lst: int list list) : int list list =
  try
    let line = (String.fold_right (fun c lst -> (int_of_char c)-48::lst) (input_line ic) []) in
    (load_input ic (lst@[line]))
  with e ->
    lst

let rec count_column_ones (bits : int list list) (column_counts: int list): int list =
  (match bits with
   | x::xs -> let new_counts = (List.fold_right2
                                  (fun bit count acc_list ->
                                    if bit = 1
                                    then (count+1)::acc_list
                                    else (count)::acc_list)
                                  x column_counts [])
              in (count_column_ones xs new_counts)
   | [] -> column_counts)
let compute_gamma (column_counts: int list) (column_length: int) : int =
  (int_of_string ("0B"^(List.fold_right (fun x s -> if x > (column_length/2) then "1"^s else "0"^s) column_counts "")))

let compute_alpha (column_counts: int list) (column_length: int) : int =
  (int_of_string ("0B"^(List.fold_right (fun x s -> if x > (column_length/2) then "0"^s else "1"^s) column_counts "")))

let predicate1 (col_length: float) (col_count: int): bool = (Float.of_int col_count) > (Float.div col_length 2.0)

let predicate2 (col_length: float) (col_count: int) : bool = not ((Float.of_int col_count) > (Float.div col_length 2.0))

(*I was originally going to do this well but my head hurts from no sleep*)
let rec filter_oxygen_rows (column_counts: int list) (column_length: float) (bits: int list list) (pred: float->int->bool) (i: int) : int list=
  let predicate = (pred column_length) in
  (match bits with
   | [] -> []
   | [x] -> x
   | x ->
      let first_row = (match bits with | x::xs -> x | _ -> []) in
      let init_list = (List.init (List.length (first_row)) (fun i -> 0)) in
      let filtered_list =
        (List.fold_right
           (fun row out_lst ->
             if ((List.nth row i) = 1 && (predicate (List.nth column_counts i)))
             then (row::out_lst)
             else if (List.nth row i) = 1 &&
                       ((Float.of_int (List.nth column_counts i)) = (Float.div column_length 2.))
             then (row::out_lst)
             else if (List.nth row i) = 0 && ((Float.of_int (List.nth column_counts i)) < (Float.div column_length 2.))
             then (row::out_lst)
             else out_lst) x []) in
      let new_column_counts = (count_column_ones filtered_list init_list) in
      (filter_oxygen_rows new_column_counts (Float.of_int (List.length filtered_list)) filtered_list pred (i+1)))

let rec filter_co2_rows (column_counts: int list) (column_length: float) (bits: int list list) (pred: float->int->bool) (i: int) : int list=
  (match bits with
   | [] -> []
   | [x] -> x
   | x ->
      let first_row = (match bits with | x::xs -> x | _ -> []) in
      let init_list = (List.init (List.length (first_row)) (fun i -> 0)) in
      let filtered_list =
        (List.fold_right
           (fun row out_lst ->
             if ((List.nth row i) = 1 && ((Float.of_int (List.nth column_counts i)) < (Float.div column_length 2.)))
             then (row::out_lst)
             else if (List.nth row i) = 0 &&
                       ((Float.of_int (List.nth column_counts i)) = (Float.div column_length 2.))
             then (row::out_lst)
             else if (List.nth row i) = 0 && ((Float.of_int (List.nth column_counts i)) > (Float.div column_length 2.))
             then (row::out_lst)
             else out_lst) x []) in
      let new_column_counts = (count_column_ones filtered_list init_list) in
      (filter_co2_rows new_column_counts (Float.of_int (List.length filtered_list)) filtered_list pred (i+1)))

let solution1 (file_name: string) : int =
  let bits = (load_input (open_in file_name) []) in
  let first_row = (match bits with | x::xs -> x | _ -> []) in
  let init_list = (List.init (List.length (first_row)) (fun i -> 0)) in
  let column_one_counts = (count_column_ones bits init_list) in
  let gamma = (compute_gamma column_one_counts (List.length bits)) in
  let alpha = (compute_alpha column_one_counts (List.length bits)) in
  gamma*alpha

let int_of_bit_list (bits: int list): int =
  (int_of_string ("0B"^(List.fold_right (fun d acc -> (string_of_int d)^acc) bits "")))

let solution2 (file_name: string) =
  let bits = (load_input (open_in file_name) []) in
  let first_row = (match bits with | x::xs -> x | _ -> []) in
  let init_list = (List.init (List.length (first_row)) (fun i -> 0)) in
  let column_one_counts = (count_column_ones bits init_list) in
  let oxy_rating = (filter_oxygen_rows column_one_counts (Float.of_int (List.length bits)) bits predicate1 0) in
  let co2_rating = (filter_co2_rows column_one_counts (Float.of_int (List.length bits)) bits predicate2 0) in
  (int_of_bit_list oxy_rating) * (int_of_bit_list co2_rating)
