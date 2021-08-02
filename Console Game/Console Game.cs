using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int pl1_x = 0;
            int pl1_y = 2;

            int pl2_x = 100;
            int pl2_y = 20;

            bool isPlayer1Chaser = true;

            int score = 0;
            bool chaseCooldown = false;

            int minX = 0;
            int maxX = 100;

            int minY = 2;
            int maxY = 20;

            while (true)
            {
                //Draw player
                Console.Clear();

                DrawHUD(isPlayer1Chaser, score);
                DrawPlayer(pl2_x, pl2_y, "X");
                DrawPlayer(pl1_x, pl1_y, "O");

                //Handle input
                ConsoleKeyInfo pressedKey = Console.ReadKey(true);

                pl1_x = HandleAxis(pl1_x, minX, maxX, pressedKey: pressedKey.Key, ConsoleKey.D, ConsoleKey.A);
                pl1_y = HandleAxis(pl1_y, minY, maxY, pressedKey: pressedKey.Key, ConsoleKey.S, ConsoleKey.W);

                pl2_x = HandleAxis(pl2_x, minX, maxX, pressedKey: pressedKey.Key, ConsoleKey.RightArrow, ConsoleKey.LeftArrow);
                pl2_y = HandleAxis(pl2_y, minY, maxY, pressedKey: pressedKey.Key, ConsoleKey.DownArrow, ConsoleKey.UpArrow);

                //Handle game logic

                //Catch detect
                if ((pl1_x == pl2_x && pl1_y == pl2_y) && !chaseCooldown)
                {

                    score++;

                    isPlayer1Chaser = !isPlayer1Chaser;
                    chaseCooldown = true;

                }
                if (chaseCooldown)
                {
                    int diffX = Math.Abs(pl1_x - pl2_x);
                    int diffY = Math.Abs(pl1_y - pl2_y);

                    int diff = diffX + diffY;

                    if (diff > 3)
                    { //escape
                        chaseCooldown = false;
                    }
                }

            }

        }

        static void DrawHUD(bool isPlayer1Chaser, int score)
        {
            Console.SetCursorPosition(0, 0);
            if (isPlayer1Chaser)
                Console.Write("Score: " + score + " Chaser: Player 1 (X)");
            else
                Console.Write("Score: " + score + " Chaser: Player 2 (O)");
            Console.SetCursorPosition(0, 1);
            Console.WriteLine("========================================");
        }
        static int HandleAxis(int axis, int min, int max, ConsoleKey pressedKey, ConsoleKey positiveKey, ConsoleKey negativeKey)
        {
            if (pressedKey == positiveKey)
                axis++;
            else if (pressedKey == negativeKey)
                axis--;

            if (axis < min)
                axis = min;
            if (axis > max)
                axis = max;

            return axis;
        }

        static void DrawPlayer(int x, int y, string visual)
        {
            Console.CursorVisible = false;
            Console.SetCursorPosition(x, y);
            Console.Write(visual);
        }

    }
}
