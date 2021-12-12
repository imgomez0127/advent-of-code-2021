let modulo x y =
  let result = x mod y in
  if result >= 0 then result
  else result + y

let (--) i j =
    let rec aux n acc =
      if n < i then acc else aux (n-1) (n :: acc)
    in aux j []

let rec load_input (ic:in_channel) (lst: int list list) : int list list =
  try
    let line = (List.map int_of_string (String.split_on_char ',' (input_line ic))) in
    (load_input ic (lst@[line]))
  with e ->
    lst

(* Just follow the simulation *)
let rec simulate_birth (fish_timers: int list) (day: int) : int =
  (if day > 0
   then let birthing_fish_amt = (List.length (List.filter (fun x -> x = 0) fish_timers)) in
        let non_birthing_timers = (List.map (fun x -> x-1) (List.filter (fun x -> x > 0) fish_timers)) in
        let new_timers = (non_birthing_timers@(List.init birthing_fish_amt (fun x -> 6))@(List.init birthing_fish_amt (fun x -> 8))) in
        (simulate_birth new_timers (day-1))
   else (List.length fish_timers))

(* Same idea just used a O(d) algorithm (where d is the number of days) *)
(* This is done by using the counts of fishes that have a certain timer number *)
(* and following the simulation using this more efficient representation *)
(* Thus by just shifting everything its a constant time operation since there are only 8 days *)
let rec simulate_birth_counts (fish_timers: (int, int) Hashtbl.t) (day: int) : int =
  (if day > 0
   then
     let new_timers = (Hashtbl.copy fish_timers) in
     (List.fold_right
        (fun day_num _ ->
          let day_count = (Hashtbl.find fish_timers (modulo (day_num+1) 9)) in
          (Hashtbl.replace new_timers day_num day_count))
        (0--8) ());
     (Hashtbl.replace new_timers 6 ((Hashtbl.find fish_timers 7)+(Hashtbl.find fish_timers 0)));
     (simulate_birth_counts new_timers (day-1))
   else (Hashtbl.fold (fun _ count acc -> acc+count) fish_timers 0))

let count_fish (fish_timers: int list) : (int, int) Hashtbl.t =
  let fish_timer_table = (Hashtbl.create 1000)
  in
  (List.fold_right
     (fun day _ -> (Hashtbl.add fish_timer_table day 0))
     (0--8) ());
  (List.fold_right
     (fun day _ -> (Hashtbl.replace fish_timer_table day ((Hashtbl.find fish_timer_table day)+1)))
        fish_timers
        ());
  fish_timer_table

let solution1 (file_name: string) : int =
  let timers = (load_input (open_in file_name) []) in
  (match timers with
   | x::xs -> (simulate_birth x 80)
   | [] -> -1)

let solution2 (file_name: string) : int =
  let timers = (load_input (open_in file_name) []) in
  (match timers with
   | x::xs -> (simulate_birth_counts (count_fish x) 256)
   | [] -> -1)
