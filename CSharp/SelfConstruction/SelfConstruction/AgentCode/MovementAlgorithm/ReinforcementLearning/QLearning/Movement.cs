﻿using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using SelfConstruction.AgentCode.Models;
using SelfConstruction.AgentCode.MovementAlgorithm.ReinforcementLearning.Abstracts;

namespace SelfConstruction.AgentCode.MovementAlgorithm.ReinforcementLearning.QLearning
{
    public class Movement
    {
        #region Fields


        List<Position> lastActions = new List<Position>();
        private bool _decrement = false;
        private int _maxStepsWithoutBuild = new Random().Next(15,25);


        #endregion

        /// <summary>
        /// Chooses the movement action depending on last steps
        /// if there where many steps without a build, the agent should walk backwards
        /// </summary>
        /// <param name="currentPosition">The current position.</param>
        /// <returns></returns>
        public object ChooseMovementAction(Position currentPosition)
        {
            object movement = GetRandomMovementAction();
            if (!_decrement)
            {
                movement = GetRandomMovementAction();
                lastActions.Add(currentPosition);
                _decrement = lastActions.Count == _maxStepsWithoutBuild;
            }
            else if (_decrement && lastActions.Any())
            {
                movement = lastActions.Last();
                lastActions.Remove(lastActions.Last());
            }
            else 
            {
                _decrement = false;
                lastActions = new List<Position>();
                movement = GetRandomMovementAction();
                lastActions.Add(currentPosition);

            }
            Console.WriteLine(movement.ToString());
            return movement;
        }


        /// <summary>
        /// Resets the stepcounter because of a buildaction
        /// </summary>
        public void ResetCauseOfBuild()
        {
            _decrement = false;
            lastActions = new List<Position>();
            _maxStepsWithoutBuild = new Random().Next(5,40);
        }

        /// <summary>
        /// Gets the random movement action.
        /// </summary>
        /// <returns></returns>
        private MovementAction GetRandomMovementAction()
        {
            Array values = Enum.GetValues(typeof(MovementAction));
            Random random = new Random();
            return (MovementAction) values.GetValue(random.Next(values.Length));
        }
        
    }
}
